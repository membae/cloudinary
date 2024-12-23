import React from 'react'
import {Route,Routes} from 'react-router-dom'
import Upload from './components/Upload'

function App() {
  return (
    <div>
      <Routes>
        <Route path="upload" element={<Upload/>}></Route>
      </Routes>
    </div>
  )
}

export default App