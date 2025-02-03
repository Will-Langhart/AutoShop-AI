import React from 'react';
import Link from 'next/link';

export default function Home() {
    return (
        <div className="container">
            <h1>Welcome to AutoShop AI</h1>
            <p>AI-powered Shopify store generation in minutes.</p>
            <Link href="/store-builder">
                <button>Get Started</button>
            </Link>
        </div>
    );
}
