interface FormStatus {
	name: string;
	status: "Incomplete" | "Complete";
}

const forms: FormStatus[] = [
	{ name: "Human Design", status: "Complete" },
	{ name: "MBTI", status: "Incomplete" },
	{ name: "Compatibility", status: "Incomplete" },
	{ name: "Zodiac", status: "Incomplete" },
];

export default function FormProgress() {
	return (
		<div className="bg-white dark:bg-gray-800 rounded p-4 shadow space-y-2">
			<h2 className="text-lg font-semibold">Form Progress</h2>
			<ul className="space-y-1">
				{forms.map((form) => (
					<li key={form.name} className="flex justify-between text-sm">
						<span>{form.name}</span>
						<span
							className={`font-medium ${
								form.status === "Complete"
									? "text-green-600"
									: "text-yellow-500"
							}`}
						>
							{form.status}
						</span>
					</li>
				))}
			</ul>
		</div>
	);
}
