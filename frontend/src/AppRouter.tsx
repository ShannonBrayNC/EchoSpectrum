import React from 'react';
import { BrowserRouter, Link, Route, Routes } from 'react-router-dom';

import CommandCenter from './CommandCenter';
import ReplayExplorer from './routes/ReplayExplorer';
import GovernanceView from './routes/GovernanceView';
import MeshDashboard from './routes/MeshDashboard';

export default function AppRouter() {
  return (
    <BrowserRouter>
      <div style={{ background: '#050816', minHeight: '100vh', color: '#d7e3ff' }}>
        <nav style={{ padding: 16, borderBottom: '1px solid #24365f', display: 'flex', gap: 16 }}>
          <Link to="/">Command Center</Link>
          <Link to="/replay">Replay Explorer</Link>
          <Link to="/mesh">Mesh Dashboard</Link>
          <Link to="/governance">Governance</Link>
        </nav>

        <Routes>
          <Route path="/" element={<CommandCenter />} />
          <Route path="/replay" element={<ReplayExplorer />} />
          <Route path="/mesh" element={<MeshDashboard />} />
          <Route path="/governance" element={<GovernanceView />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}
