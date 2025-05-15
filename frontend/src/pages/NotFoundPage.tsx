import { Link } from "react-router-dom";

export default function NotFoundPage() {
	return (
		<div className="text-center py-20 animate-bounce-fade">
			<h1 className="text-6xl font-extrabold text-gray-800 dark:text-gray-200">404</h1>
			<p className="mt-4 text-xl text-gray-600 dark:text-gray-400">
				Oops! Page not found.
			</p>
			<Link
				to="/"
				className="mt-6 inline-block bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 transition"
			>
				Go back home
			</Link>
		</div>
	);
}
