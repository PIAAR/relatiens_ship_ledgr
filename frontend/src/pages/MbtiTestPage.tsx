export default function MbtiTestPage() {
	return (
		<div className="space-y-6">
			<h1 className="text-2xl font-bold">MBTI Personality Test</h1>
			<p className="text-gray-600 dark:text-gray-300">
				Answer a few questions to discover your Myers-Briggs type and cognitive
				functions.
			</p>

			<div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
				<p className="text-sm text-gray-500 dark:text-gray-400">
					The MBTI test helps you understand your mental preferences across four
					dichotomies:
				</p>
				<ul className="list-disc pl-6 mt-4 text-gray-600 dark:text-gray-300 text-sm">
					<li>Introversion (I) / Extraversion (E)</li>
					<li>Sensing (S) / Intuition (N)</li>
					<li>Thinking (T) / Feeling (F)</li>
					<li>Judging (J) / Perceiving (P)</li>
				</ul>

				<div className="mt-6">
					<button className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 transition">
						Start MBTI Quiz
					</button>
				</div>
			</div>
		</div>
	);
}
