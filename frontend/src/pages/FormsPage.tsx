import { Link } from "react-router-dom";

export default function FormsPage() {
	const tests = [
		{
			title: "Human Design",
			description: "Energy type, authority, profile.",
			link: "/human-design",
			status: "Complete", // ← Use quiz engine data later
		},
		{
			title: "MBTI Personality",
			description: "Get your 4-letter type and cognitive functions.",
			link: "/mbti",
			status: "Incomplete",
		},
		{
			title: "Compatibility",
			description: "Measure values and emotional fit.",
			link: "/compatibility",
			status: "Incomplete",
		},
		{
			title: "Zodiac",
			description: "Astrological insights (sun, moon, rising).",
			link: "/zodiac",
			status: "Incomplete",
		},
	];

	return (
		<div className="space-y-6">
			<h1 className="text-2xl font-bold">Forms & Tests</h1>
			<p className="text-gray-600 dark:text-gray-300">
				Choose a test below to get started.
			</p>

			<div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
				{tests.map((test) => (
					<Link
						key={test.title}
						to={test.link}
						className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow hover:shadow-lg transition transform hover:-translate-y-1"
					>
						<h2 className="text-lg font-semibold mb-2">{test.title}</h2>
						<p className="text-sm text-gray-500 dark:text-gray-400">
							{test.description}
						</p>

						{/* ✅ Insert the status badge here */}
						<div className="mt-3">
							<span
								className={`inline-block px-3 py-1 text-xs rounded-full ${
									test.status === "Complete"
										? "bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200"
										: "bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200"
								}`}
							>
								{test.status}
							</span>
						</div>
					</Link>
				))}
			</div>
		</div>
	);
}
