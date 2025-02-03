import React, { useState } from "react";

export default function StoreBuilder() {
    const [storeName, setStoreName] = useState("");
    const [email, setEmail] = useState("");
    const [message, setMessage] = useState("");

    const createStore = async () => {
        const response = await fetch("http://127.0.0.1:5002/store/create", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ store_name: storeName, owner_email: email })
        });

        const data = await response.json();
        setMessage(data.message);
    };

    return (
        <div className="container">
            <h2>Create Your AI-Generated Shopify Store</h2>
            <input type="text" placeholder="Store Name" value={storeName} onChange={(e) => setStoreName(e.target.value)} />
            <input type="email" placeholder="Your Email" value={email} onChange={(e) => setEmail(e.target.value)} />
            <button onClick={createStore}>Create Store</button>
            <p>{message}</p>
        </div>
    );
}
