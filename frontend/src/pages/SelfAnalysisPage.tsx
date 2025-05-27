// frontend/src/pages/SelfAnalysisPage.tsx
export default function SelfAnalysisPage() {
	const categories = [
		{
			title: "Emotional Patterns",
			description: "Your instinctual response to emotional intensity and energy flow.",
			traits: ["Suppression", "Overexpression", "Mood Regulation"],
		},
		{
			title: "Coping Tendencies",
			description: "How you maintain control or safety in stressful moments.",
			traits: ["Avoidance", "Control Seeking", "Self-Soothing"],
		},
		{
			title: "Attachment Behavior",
			description: "Your pattern of bonding, reassurance seeking, or withdrawal.",
			traits: ["Anxious Attachment", "Secure Base Seeking", "Avoidant Patterns"],
		},
	];

	return (
		<div className="space-y-8">
			<header className="text-center">
				<h1 className="text-3xl font-bold text-indigo-900 dark:text-purple-300">
					Know Thyself
				</h1>
				<p className="text-sm text-gray-500 dark:text-gray-400 mt-2">
					Your self-awareness is your crown. Wear it wisely.
				</p>
			</header>

			{categories.map((cat, idx) => (
				<section
					key={idx}
					className="bg-white dark:bg-[#1e1b4b] p-6 rounded-xl shadow-md border border-purple-200 dark:border-purple-700"
				>
					<h2 className="text-xl font-semibold text-indigo-800 dark:text-pink-300">
						{cat.title}
					</h2>
					<p className="text-sm text-gray-600 dark:text-gray-300 mt-1">
						{cat.description}
					</p>

					<div className="mt-4 space-y-2">
						{cat.traits.map((trait, tidx) => (
							<div
								key={tidx}
								className="flex justify-between items-center py-2 border-b border-gray-100 dark:border-gray-700"
							>
								<span className="text-sm text-gray-700 dark:text-gray-200">
									{trait}
								</span>
								<span className="text-xs px-3 py-1 bg-purple-100 text-purple-900 rounded-full dark:bg-purple-700 dark:text-white">
									Tap for Insight
								</span>
							</div>
						))}
					</div>
				</section>
			))}
		</div>
	);
}
