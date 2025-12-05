import { BrowserRouter } from 'react-router-dom'
import Button from './components/Button'
import SignupForm from './pages/Signup'

export default function MyApp() {
    return (
        <>
            <p className="text-red-500">This is MyApp</p>
            <Button />
            <SignupForm />
        </>
    )
}