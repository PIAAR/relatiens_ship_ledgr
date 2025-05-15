/** @type {import('tailwindcss').Config} */
module.exports = {
	darkMode: "class", // ← Required
	content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
	theme: {
		extend: {
			animation: {
				"bounce-fade": "bounceFade 1s ease-out",
			},
			keyframes: {
				bounceFade: {
					"0%": { opacity: "0", transform: "scale(0.95) translateY(-30px)" },
					"60%": { opacity: "0.75", transform: "scale(1.05) translateY(10px)" },
					"100%": { opacity: "1", transform: "scale(1) translateY(0)" },
				},
			},
		},
	},
	plugins: [],
};
