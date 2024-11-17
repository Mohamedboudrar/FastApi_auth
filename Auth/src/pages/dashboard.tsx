import { Button } from "@/components/ui/button"
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from "@/components/ui/card"
import { LogOut } from 'lucide-react'

interface DashboardProps {
  username: string
  onLogout: () => void
}

export function Dashboard({ onLogout }: DashboardProps) {
  return (
    <Card className="w-[350px] mx-auto mt-40">
      <CardHeader>
        <CardTitle>Dashboard</CardTitle>
        <CardDescription>Welcome to your account</CardDescription>
      </CardHeader>
      <CardContent>
        <p className="text-center mb-4">Hello !</p>
        <Button onClick={onLogout} className="w-full">
          <LogOut className="mr-2 h-4 w-4" /> Logout
        </Button>
      </CardContent>
    </Card>
  )
}