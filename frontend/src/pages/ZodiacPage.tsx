export default function ZodiacPage() {
	return (
		<div className="space-y-6">
			<h1 className="text-2xl font-bold">Zodiac Insights</h1>
			<p className="text-gray-600 dark:text-gray-300">
				Understand yourself and your relationships through your zodiac sun, moon, and
				rising signs.
			</p>

			<div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow space-y-4">
				<p className="text-sm text-gray-500 dark:text-gray-400">
					We use your birth date, time, and location to calculate your astrological
					chart.
				</p>

				<button className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 transition">
					Start Zodiac Reading
				</button>
			</div>
		</div>
	);
}
