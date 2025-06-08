// frontend/src/components/BottomNav.tsx
import { FileText, Gem, Home, MessageCircle, User } from "lucide-react";
import { Link, useLocation } from "react-router-dom";

export default function BottomNav() {
	const location = useLocation();

	const navItems = [
		{ to: "/", icon: <Home className="w-5 h-5" />, label: "Home" },
		{ to: "/forms", icon: <FileText className="w-5 h-5" />, label: "Forms" },
		{ to: "/the-table", icon: <Gem className="w-5 h-5" />, label: "The Table" },
		{ to: "/chat", icon: <MessageCircle className="w-5 h-5" />, label: "Chat" },
		{ to: "/self-analysis", icon: <User className="w-5 h-5" />, label: "Profile" },
	];

	return (
		<nav className="fixed bottom-0 inset-x-0 z-80 bg-white dark:bg-[#1e1b4b] border-t border-gray-200 dark:border-purple-700 shadow-md md:hidden">
			<div className="flex justify-around px-4 py-2">
				{navItems.map((item) => {
					const active = location.pathname === item.to;
					return (
						<Link
							key={item.to}
							to={item.to}
							className={`flex flex-col items-center text-xs ${
								active
									? "text-indigo-600 dark:text-pink-300"
									: "text-gray-500 dark:text-gray-300"
							}`}
						>
							{item.icon}
							<span>{item.label}</span>
						</Link>
					);
				})}
			</div>
		</nav>
	);
}
