import React, { useState } from "react";

function SignupForm() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log("inputs:", { username, password });

        // call to api
    };

    return (
        <form onSubmit={handleSubmit} style={{ maxWidth: "300px" }}>
            <h2>Sign Up</h2>

            <label>
                Username<br />
                <input type="text" value={username} onChange={(e) => setUsername(e.target.value)}required />
            </label>

            <label>
                Password<br />
                <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
            </label>

            <button type="submit">Sign Up</button>
        </form>
    );
}

export default SignupForm;
