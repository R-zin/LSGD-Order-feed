import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import './index.css'
import Hero from './Pages/Hero'
import Orders from './Pages/Orders'
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <div className= 'min-h-screen'>
      <Hero></Hero>
    </div>
    <div className='min-h-screen'>
    <Orders></Orders>
    </div>
    </>
  )
}

export default App;
