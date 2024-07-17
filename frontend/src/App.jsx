import React from 'react'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Home from './components/Home'
import Register from './components/Register'
import Login from './components/Login'
import Resetpassform from './components/Resetpassform'
import ResetPassEmail from './components/ResetPassEmail'
import UserProfile from './components/UserProfile'
import ProtectedRoute from './components/ProtectedRoute' // it is used to protect routes without logged-in
import SpecialProtect from './components/SpecialProtect' // it is used to protect Login page while logged-in
import Changepass from './components/Changepass'

const App = () => {
  return (
    <BrowserRouter>
    <Routes>
      <Route path='/' element={<ProtectedRoute><Home /></ProtectedRoute>}/>
      <Route path='/Register' Component={Register}/>
      <Route path='/Login' element={<SpecialProtect><Login /></SpecialProtect>}/>
      <Route path='/change-pass' Component={Changepass}/>
      <Route path='/reset-pass' Component={ResetPassEmail}/>
      <Route path='/reset-password/:uid/:token' Component={Resetpassform}/>
      <Route path='/userprofile' Component={UserProfile}/>
    </Routes>
    </BrowserRouter>
  )
}

export default App