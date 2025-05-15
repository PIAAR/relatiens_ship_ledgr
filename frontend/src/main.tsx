import "./index.css";

import { BrowserRouter, Route, Routes } from "react-router-dom";
import React, { Suspense, lazy } from "react";

import ReactDOM from "react-dom/client";
import SidebarLayout from "./components/SidebarLayout";

const HomePage = lazy(() => import("./pages/HomePage"));
const HumanDesignPage = lazy(() => import("./pages/HumanDesignPage"));
const NotFoundPage = lazy(() => import("./pages/NotFoundPage"));
const DashboardPage = lazy(() => import("./pages/DashboardPage"));
const FormsPage = lazy(() => import("./pages/FormsPage"));
const MbtiTestPage = lazy(() => import("./pages/MbtiTestPage"));
const CompatibilityTestPage = lazy(() => import("./pages/CompatibilityTestPage"));
const ZodiacPage = lazy(() => import('./pages/ZodiacPage'));


ReactDOM.createRoot(document.getElementById("root")!).render(
	<React.StrictMode>
		<BrowserRouter>
			<Suspense fallback={<div className="p-6 text-gray-500">Loading...</div>}>
				<Routes>
					<Route path="/" element={<SidebarLayout />}>
						<Route index element={<DashboardPage />} />
						<Route path="forms" element={<FormsPage />} />
						<Route path="human-design" element={<HumanDesignPage />} />
            <Route path="mbti" element={<MbtiTestPage />} />
            <Route path="zodiac" element={<ZodiacPage />} />
						<Route path="compatibility" element={<CompatibilityTestPage />} />
						<Route path="*" element={<NotFoundPage />} />
					</Route>
				</Routes>
			</Suspense>
		</BrowserRouter>
	</React.StrictMode>
);
