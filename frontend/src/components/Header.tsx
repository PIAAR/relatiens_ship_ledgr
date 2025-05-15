import { useLocation } from "react-router-dom";

export default function Header() {
	const location = useLocation();

	const crumbs = location.pathname
		.split("/")
		.filter(Boolean)
		.map((crumb, idx, arr) => ({
			name: crumb.charAt(0).toUpperCase() + crumb.slice(1),
			path: "/" + arr.slice(0, idx + 1).join("/"),
		}));

	return (
		<header className="w-full bg-white dark:bg-gray-800 shadow px-4 py-3 flex items-center justify-between">
			<div className="text-sm text-gray-500 dark:text-gray-400">
				{crumbs.length === 0 ? (
					<span className="font-medium text-gray-800 dark:text-gray-100">
						Dashboard
					</span>
				) : (
					crumbs.map((c, i) => (
						<span key={c.path}>
							<span className="text-gray-400">/</span>
							<span className="ml-1 font-medium text-gray-800 dark:text-gray-100">
								{c.name}
							</span>
						</span>
					))
				)}
			</div>
		</header>
	);
}
