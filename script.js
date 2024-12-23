let questions; // 问题数组  
let currentQuestion = 0; // 当前题号  
let score = 0; // 计分  

// 加载字典问题数据  
fetch('questions.json')  
  .then(res => res.json())  
  .then(data => {  
    questions = data;  
    loadQuestion();  
  })  
  .catch(err => console.error('Failed to load questions:', err));  

// 加载题目  
function loadQuestion() {  
  const questionBox = document.getElementById("question-text");  
  const optionsBox = document.getElementById("answer-options");  
  const nextButton = document.getElementById("next-button");  
  const feedback = document.getElementById("feedback");  

  feedback.textContent = ""; // 清空反馈信息  
  nextButton.classList.add("hidden"); // 隐藏下一题按钮  
  optionsBox.innerHTML = "";  

  if (currentQuestion >= questions.length) {  
    questionBox.textContent = "🎉 恭喜你完成了所有问题！";  
    optionsBox.innerHTML = `<p>您的最终得分是: <strong>${score}</strong> / ${questions.length}</p>`;  
    return;  
  }  

  const question = questions[currentQuestion];  
  questionBox.textContent = question.prompt;  

  // 根据题型生成选项  
  if (question.type === "choice") {  
    question.options.forEach(option => {  
      const button = document.createElement("button");  
      button.textContent = option;  
      button.addEventListener("click", () => checkAnswer(option));  
      optionsBox.appendChild(button);  
    });  
  } else if (question.type === "fill-in") {  
    const input = document.createElement("input");  
    input.type = "text";  
    input.placeholder = "输入答案";  
    const submitButton = document.createElement("button");  
    submitButton.textContent = "提交";  
    submitButton.addEventListener("click", () => checkAnswer(input.value));  
    optionsBox.appendChild(input);  
    optionsBox.appendChild(submitButton);  
  }  
}  

// 检查用户答案  
function checkAnswer(answer) {  
  const question = questions[currentQuestion];  
  const feedback = document.getElementById("feedback");  
  const nextButton = document.getElementById("next-button");  

  if (answer.trim().toLowerCase() === question.answer.trim().toLowerCase()) {  
    score++;  
    feedback.textContent = "✔️ 回答正确！";  
    feedback.className = "correct";  
  } else {  
    feedback.textContent = `❌ 回答错误！正确答案是：${question.answer}`;  
    feedback.className = "wrong";  
  }  

  document.getElementById("score").textContent = `得分: ${score}`;  
  nextButton.classList.remove("hidden");  
  nextButton.onclick = () => {  
    currentQuestion++;  
    loadQuestion();  
  };  
}