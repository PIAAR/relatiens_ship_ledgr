import HumanDesignForm from "../components/HumanDesignForm";
import HumanDesignResult from "../components/HumanDesignResult";
import Spinner from "../components/Spinner";
import { useState } from "react";

export default function HumanDesignPage() {
	const [result, setResult] = useState<any | null>(null);
	const [loading, setLoading] = useState(false);
	const [error, setError] = useState("");

	const handleSubmit = async (formData: any) => {
		setLoading(true);
		setError("");

		try {
			const response = await fetch("/api/human-design/report", {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				body: JSON.stringify(formData),
			});

			if (!response.ok) throw new Error("API error");

			const data = await response.json();
			setResult(data);
		} catch (err) {
			setError("Something went wrong. Showing mock data.");
			setResult({
				type: "Generator",
				authority: "Emotional",
				profile: "4/6",
				defined_centers: ["Sacral", "Root"],
				open_centers: ["Heart", "Head"],
				gates: [2, 3, 4],
				channels: ["2-14", "3-60"],
				summary: "You are a Generator with Emotional authority...",
			});
		} finally {
			setLoading(false);
		}
	};

	return (
		<div className="p-6">
			<h2 className="text-2xl font-semibold mb-4">Human Design Chart</h2>
			<HumanDesignForm onSubmit={handleSubmit} />
			{loading && <Spinner />}
			{error && <p className="text-red-500 mt-2">{error}</p>}
			<HumanDesignResult data={result} />
		</div>
	);
}
