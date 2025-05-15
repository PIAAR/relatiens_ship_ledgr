import { Link, Outlet, useLocation } from "react-router-dom";
import { useEffect, useState } from "react";

import ThemeToggle from "./ThemeToggle";

export default function Layout() {
	const [menuOpen, setMenuOpen] = useState(false);
	const location = useLocation();

	// Auto-close menu on route change
	useEffect(() => {
		setMenuOpen(false);
	}, [location.pathname]);

	return (
		<div className="min-h-screen bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-white">
			{/* Header */}
			<header className="bg-white dark:bg-gray-800 shadow-md sticky top-0 z-20">
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
			</header>

			{/* Side Drawer Menu */}
			<div
				className={`fixed top-0 left-0 h-full w-64 bg-white dark:bg-gray-800 shadow-lg transform transition-transform duration-300 ease-in-out z-40 ${
					menuOpen ? "translate-x-0" : "-translate-x-full"
				} md:hidden`}
			>
				<div className="p-4 space-y-4 pt-20">
					<Link to="/" className="block text-lg hover:underline">
						Home
					</Link>
					<Link to="/human-design" className="block text-lg hover:underline">
						Human Design
					</Link>
					<div className="pt-4 border-t border-gray-300 dark:border-gray-600">
						<ThemeToggle />
					</div>
				</div>
			</div>

			{/* Backdrop */}
			{menuOpen && (
				<div
					onClick={() => setMenuOpen(false)}
					className="fixed inset-0 bg-black bg-opacity-40 z-30 md:hidden"
				/>
			)}

			{/* Page Content */}
			<main className="max-w-5xl mx-auto p-6 relative z-0">
				<Outlet />
			</main>
		</div>
	);
}
