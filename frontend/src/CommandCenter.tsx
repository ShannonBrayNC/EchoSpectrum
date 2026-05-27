import React from 'react';

const nodes = [
  { id: 'node-rdu-001', status: 'healthy', location: 'Raleigh, NC' },
  { id: 'node-fay-002', status: 'healthy', location: 'Fayetteville, NC' },
  { id: 'node-gso-003', status: 'warning', location: 'Greensboro, NC' },
];

export default function CommandCenter() {
  return (
    <div style={{ padding: 24, color: '#d7e3ff', background: '#050816', minHeight: '100vh' }}>
      <h1>Lantern Protocol Observatory Command Center</h1>
      <p>Federated EchoSpectrum mesh coordination console</p>

      <div style={{ marginTop: 24 }}>
        <h2>Distributed Observatory Nodes</h2>
        {nodes.map(node => (
          <div key={node.id} style={{ border: '1px solid #24365f', borderRadius: 10, padding: 12, marginTop: 12 }}>
            <strong>{node.id}</strong>
            <div>Status: {node.status}</div>
            <div>Location: {node.location}</div>
          </div>
        ))}
      </div>

      <div style={{ marginTop: 32, border: '1px solid #4f1f1f', padding: 16, borderRadius: 10 }}>
        <strong>ETS Governance Overlay Active</strong>
        <p>RX-only distributed observatory enforcement enabled.</p>
      </div>

      <div style={{ marginTop: 32 }}>
        <h2>Replay Sessions</h2>
        <ul>
          <li>915 MHz ISM survey replay</li>
          <li>ADS-B directional observation replay</li>
          <li>2.4 GHz occupancy replay</li>
        </ul>
      </div>
    </div>
  );
}
