import React from 'react';

const sessions = [
  {
    id: 'replay-915mhz',
    title: '915 MHz ISM Survey',
    duration: '12m',
  },
  {
    id: 'replay-adsb',
    title: 'ADS-B Observation Session',
    duration: '22m',
  },
  {
    id: 'replay-24ghz',
    title: '2.4 GHz Occupancy Replay',
    duration: '9m',
  },
];

export default function ReplayExplorer() {
  return (
    <div style={{ padding: 24, color: '#d7e3ff', background: '#050816', minHeight: '100vh' }}>
      <h1>Replay Explorer</h1>
      <p>Replay-aware observatory session navigation.</p>

      <div style={{ marginTop: 24 }}>
        {sessions.map(session => (
          <div key={session.id} style={{ border: '1px solid #24365f', borderRadius: 10, padding: 16, marginTop: 12 }}>
            <strong>{session.title}</strong>
            <div>Duration: {session.duration}</div>
            <button style={{ marginTop: 12 }}>Open Replay</button>
          </div>
        ))}
      </div>
    </div>
  );
}
