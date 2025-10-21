import React, { useState, useEffect } from 'react'
import './App.css'

function App() {
  // 1. 状态包含 num1、num2、response、score，初始值 num1:1、num2:1、response:""、score:0
  const [num1, setNum1] = useState(1)
  const [num2, setNum2] = useState(1)
  const [response, setResponse] = useState('')
  const [score, setScore] = useState(0)

  // 3. updateResponse 函数，用来更新 response 的状态
  const updateResponse = (e) => {
    setResponse(e.target.value)
  }

  // 4. inputKeyPress 函数：按下Enter键时判断输入
  const inputKeyPress = (e) => {
    if (e.key === 'Enter') {
      const userAnswer = parseInt(response)
      const correctAnswer = num1 + num2

      if (userAnswer === correctAnswer) {
        // 正确：得分+1，生成1-10的新随机数，清空输入框
        setScore(score + 1)
        setNum1(Math.floor(Math.random() * 10) + 1)
        setNum2(Math.floor(Math.random() * 10) + 1)
        setResponse('')
      } else {
        // 错误：得分-1，清空输入框
        setScore(Math.max(0, score - 1))
        setResponse('')
      }
    }
  }

  return (
    <div className="app">
      <div className="game-container">
        {/* 2. 页面显示 num1 + num2 的算式 */}
        <div id="problem" className="problem">
          {num1} + {num2} = ?
        </div>

        {/* 输入框 */}
        <div className="input-section">
          <input
            type="number"
            value={response}
            onChange={updateResponse}
            onKeyPress={inputKeyPress}
            placeholder="输入答案"
            className="answer-input"
            autoFocus
          />
        </div>

        {/* 2. 当前得分 */}
        <div className="score-section">
          <div className="score">得分: {score}</div>
        </div>

        {/* 6. 当得分等于10时，显示"You won!" */}
        {score === 10 && (
          <div id="winner" className="winner-message">
            You won!
          </div>
        )}
      </div>
    </div>
  )
}

export default App