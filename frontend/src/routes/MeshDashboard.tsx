import React from 'react';

const nodes = [
  { id: 'node-rdu-001', health: 'healthy' },
  { id: 'node-fay-002', health: 'healthy' },
  { id: 'node-gso-003', health: 'warning' },
];

export default function MeshDashboard() {
  return (
    <div style={{ padding: 24, color: '#d7e3ff', background: '#050816', minHeight: '100vh' }}>
      <h1>Mesh Dashboard</h1>
      <p>Distributed observatory node health and telemetry visibility.</p>

      {nodes.map(node => (
        <div key={node.id} style={{ border: '1px solid #24365f', borderRadius: 10, padding: 16, marginTop: 12 }}>
          <strong>{node.id}</strong>
          <div>Health: {node.health}</div>
        </div>
      ))}
    </div>
  );
}
