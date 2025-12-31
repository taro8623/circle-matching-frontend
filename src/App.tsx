import { BrowserRouter, Routes, Route } from "react-router-dom";
import CircleRegister from "./pages/CircleRegister";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/register" element={<CircleRegister />} />
      </Routes>
    </BrowserRouter>
  );
}
