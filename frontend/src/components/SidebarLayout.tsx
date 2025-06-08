// frontend/src/components/SidebarLayout.tsx
import { Outlet, useLocation } from "react-router-dom";
import { useEffect, useState } from "react";

import BottomNav from "./BottomNav";
import Header from "./Header";
import Sidebar from "./Sidebar";

export default function SidebarLayout() {
	const [mobileOpen, setMobileOpen] = useState(false);
	const location = useLocation();

	useEffect(() => {
		setMobileOpen(false);
	}, [location.pathname]);

	return (
		<div className="flex flex-col min-h-screen bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-white">
			{/* Desktop Sidebar - Optional: add fixed sidebar layout later */}
			<div className="hidden md:block">
				<Sidebar />
			</div>

			{/* Mobile Sidebar Drawer */}
			<div className="md:hidden">
				{mobileOpen && (
					<>
						<div
							className="fixed inset-0 bg-black bg-opacity-50 z-40"
							onClick={() => setMobileOpen(false)}
						/>
						<div className="fixed z-50 top-0 left-0 h-full w-64 bg-white dark:bg-gray-800 shadow-md transition-transform">
							<Sidebar />
						</div>
					</>
				)}
				<button
					onClick={() => setMobileOpen(true)}
					className="absolute top-4 left-4 z-50 text-gray-800 dark:text-gray-100"
				>
					<svg
						className="w-6 h-6"
						fill="none"
						stroke="currentColor"
						viewBox="0 0 24 24"
					>
						<path
							strokeLinecap="round"
							strokeLinejoin="round"
							strokeWidth={2}
							d="M4 6h16M4 12h16M4 18h16"
						/>
					</svg>
				</button>
			</div>

			{/* Main Content */}
			<div className="flex-1 flex flex-col overflow-hidden">
				<Header />
				<main className="flex-1 overflow-y-auto p-6 pb-28">
					<Outlet />
				</main>
				{/* Spacer to prevent nav overlap */}
				<div className="h-16 md:hidden" />
				<div className="h-[300vh] bg-gradient-to-b from-white to-black" />
				<BottomNav />
			</div>
		</div>
	);
}
