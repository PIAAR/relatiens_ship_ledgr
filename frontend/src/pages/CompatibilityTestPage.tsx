export default function CompatibilityTestPage() {
	return (
		<div className="space-y-6">
			<h1 className="text-2xl font-bold">Relationship Compatibility Test</h1>
			<p className="text-gray-600 dark:text-gray-300">
				Use this test to explore emotional, intellectual, and lifestyle alignment with a
				partner.
			</p>

			<div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
				<p className="text-sm text-gray-500 dark:text-gray-400">
					This tool calculates closeness scores based on shared values, communication
					styles, and future goals.
				</p>

				<div className="mt-6">
					<button className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 transition">
						Start Compatibility Quiz
					</button>
				</div>
			</div>
		</div>
	);
}
