// frontend/src/components/Layout.tsx
import { Link, Outlet } from "react-router-dom";

import ThemeToggle from "./ThemeToggle";
import { useState } from "react";

export default function Layout() {
	const [menuOpen, setMenuOpen] = useState(false);

	return (
		<div className="min-h-screen bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-white">
			{/* Header */}
			<header className="bg-white dark:bg-gray-800 shadow-md sticky top-0 z-10">
				<div className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
					<h1 className="text-xl font-bold">Relationship Ledger</h1>

					{/* Desktop Nav */}
					<nav className="hidden md:flex space-x-4 items-center">
						<Link to="/" className="hover:underline">
							Home
						</Link>
						<Link to="/human-design" className="hover:underline">
							Human Design
						</Link>
						<ThemeToggle />
					</nav>

					{/* Hamburger Button */}
					<div className="md:hidden flex items-center">
						<button
							onClick={() => setMenuOpen(!menuOpen)}
							className="text-gray-700 dark:text-gray-200 focus:outline-none"
							aria-label="Toggle menu"
						>
							<svg
								className="w-6 h-6"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								{menuOpen ? (
									<path
										strokeLinecap="round"
										strokeLinejoin="round"
										strokeWidth={2}
										d="M6 18L18 6M6 6l12 12"
									/>
								) : (
									<path
										strokeLinecap="round"
										strokeLinejoin="round"
										strokeWidth={2}
										d="M4 6h16M4 12h16M4 18h16"
									/>
								)}
							</svg>
						</button>
					</div>
				</div>

				{/* Mobile Menu */}
				{menuOpen && (
					<div className="md:hidden bg-white dark:bg-gray-800 px-4 pb-4 space-y-2">
						<Link to="/" className="block" onClick={() => setMenuOpen(false)}>
							Home
						</Link>
						<Link
							to="/human-design"
							className="block"
							onClick={() => setMenuOpen(false)}
						>
							Human Design
						</Link>
						<div className="pt-2 border-t border-gray-200 dark:border-gray-700">
							<ThemeToggle />
						</div>
					</div>
				)}
			</header>

			{/* Page content */}
			<main className="max-w-5xl mx-auto p-6">
				<Outlet />
			</main>
		</div>
	);
}
