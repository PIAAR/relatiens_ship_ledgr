import FormProgress from "../components/FormProgress";

export default function DashboardPage() {
	return (
		<div className="space-y-6">
			<h1 className="text-2xl font-bold">Welcome, Rahm</h1>
			<p className="text-gray-600 dark:text-gray-300">
				This is your Relationship Ledger dashboard. Explore your insights and track your
				personal growth.
			</p>

			<div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4">
				<div className="bg-white dark:bg-gray-800 p-4 rounded shadow">
					<h2 className="text-lg font-semibold">Recent Activity</h2>
					<p className="text-sm text-gray-500 dark:text-gray-400 mt-1">
						No recent activity yet.
					</p>
				</div>

				<div className="bg-white dark:bg-gray-800 p-4 rounded shadow">
					<FormProgress />
				</div>

				<div className="bg-white dark:bg-gray-800 p-4 rounded shadow">
					<h2 className="text-lg font-semibold">Your Type Summary</h2>
					<p className="text-sm text-gray-500 dark:text-gray-400 mt-1">
						Complete your forms to unlock this section.
					</p>
				</div>

				<div className="bg-white dark:bg-gray-800 p-4 rounded shadow">
					<h2 className="text-lg font-semibold">Coming Soon</h2>
					<p className="text-sm text-gray-500 dark:text-gray-400 mt-1">
						More insights and compatibility features.
					</p>
				</div>
			</div>
		</div>
	);
}
