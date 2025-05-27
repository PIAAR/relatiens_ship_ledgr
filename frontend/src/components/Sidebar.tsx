// frontend/src/components/Sidebar.tsx
import { Link } from "react-router-dom";
import ThemeToggle from "./ThemeToggle";

export default function Sidebar() {
	return (
		<aside className="h-full w-64 bg-white dark:bg-gray-800 shadow-md flex flex-col justify-between">
			{/* Branding */}
			<div>
				<div className="p-6 border-b border-gray-200 dark:border-gray-700">
					<h2 className="text-xl font-extrabold tracking-tight text-blue-600 dark:text-blue-400">
						R•Ledger
					</h2>
					<p className="text-xs mt-1 text-gray-500 dark:text-gray-400">
						by RMoor Industries
					</p>
				</div>

				{/* Navigation */}
				<nav className="p-6 space-y-4">
					<Link to="/" className="block hover:underline">
						Home
					</Link>
					<Link to="/human-design" className="block hover:underline">
						Human Design
					</Link>
				</nav>
			</div>

			{/* Footer: Profile + Theme */}
			<div className="p-6 border-t border-gray-200 dark:border-gray-700">
				<div className="text-sm mb-2">
					<p className="font-semibold">Rahm Moore</p>
					<p className="text-gray-500 dark:text-gray-400">Founder</p>
				</div>
				<ThemeToggle />
			</div>
		</aside>
	);
}
