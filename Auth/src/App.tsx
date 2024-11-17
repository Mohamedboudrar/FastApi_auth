'use client'

import { useState } from 'react'
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Login } from './pages/Login'
import { Signup } from './pages/Signup'
import { Dashboard } from './pages/dashboard'

export default function AuthFrontend() {
  const [isLoggedIn, setIsLoggedIn] = useState(false)
  const [username, setUsername] = useState('')

  const handleLogin = async (username: string, password: string) => {
    // Replace this with your actual API call
    const response = await fetch('http://127.0.0.1:8000/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password }),
    })

    if (!response.ok) {
      throw new Error('Login failed')
    }

    setIsLoggedIn(true)
    setUsername(username)
  }

  const handleSignup = async (email: string, name: string, password: string) => {
    // Replace this with your actual API call
    const response = await fetch('http://127.0.0.1:8000/signup', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, name, password }),
    })

    if (!response.ok) {
      throw new Error('Signup failed')
    }

    setIsLoggedIn(true)
    setUsername(username)
  }

  const handleLogout = () => {
    setIsLoggedIn(false)
    setUsername('')
  }

  if (isLoggedIn) {
    return <Dashboard username={username} onLogout={handleLogout} />
  }

  return (
    <Tabs defaultValue="login" className="w-[350px] mt-40 mx-auto">
      <TabsList className="grid w-full grid-cols-2">
        <TabsTrigger value="login">Login</TabsTrigger>
        <TabsTrigger value="signup">Sign Up</TabsTrigger>
      </TabsList>
      <TabsContent value="login">
        <Login onLogin={handleLogin} />
      </TabsContent>
      <TabsContent value="signup">
        <Signup onSignup={handleSignup} />
      </TabsContent>
    </Tabs>
  )
}