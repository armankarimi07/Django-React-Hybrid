import { BrowserRouter, Link, Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import SignupForm from './pages/Signup'

export default function MyApp() {
    return (
        <BrowserRouter>
            <p className="text-red-500">This is MyApp</p>
            <nav>
                <Link to="/">Home</Link>
                <Link to="/signup">Signup</Link>
            </nav>

            <Routes>
                <Route path='/' element={<Home />} />
                <Route path='/signup' element={<SignupForm />} />
            </Routes>
        </BrowserRouter>
    )
}