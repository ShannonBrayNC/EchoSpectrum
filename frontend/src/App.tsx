import React from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

const generateSpectrum = () => {
  return Array.from({ length: 64 }).map((_, i) => ({
    frequency: 900 + i,
    power: -80 + Math.sin(i / 4) * 12 + Math.random() * 6,
  }));
};

const data = generateSpectrum();

export default function App() {
  return (
    <div style={{ background: '#050816', color: '#d7e3ff', minHeight: '100vh', padding: '24px', fontFamily: 'sans-serif' }}>
      <h1>EchoSpectrum Observatory</h1>
      <p>Receive-only RF observability console</p>

      <div style={{ border: '1px solid #1e2d52', borderRadius: '12px', padding: '16px', marginTop: '24px' }}>
        <h2>Live Spectrum Scope</h2>
        <ResponsiveContainer width="100%" height={320}>
          <LineChart data={data}>
            <XAxis dataKey="frequency" />
            <YAxis />
            <Tooltip />
            <Line type="monotone" dataKey="power" dot={false} />
          </LineChart>
        </ResponsiveContainer>
      </div>

      <div style={{ marginTop: '24px', padding: '16px', border: '1px solid #4f1f1f', borderRadius: '12px', background: '#180c0c' }}>
        <strong>Compliance Mode:</strong> RX-ONLY
        <br />
        Jamming, packet injection, deauthentication, and unauthorized transmission are prohibited.
      </div>

      <div style={{ marginTop: '24px', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '16px' }}>
        <div style={{ border: '1px solid #1e2d52', borderRadius: '12px', padding: '16px' }}>
          <h3>Session Metadata</h3>
          <ul>
            <li>Center Frequency: 915 MHz</li>
            <li>Sample Rate: 10 Msps</li>
            <li>Antenna: Proxicast LPDA</li>
            <li>Sensor: HackRF One</li>
          </ul>
        </div>

        <div style={{ border: '1px solid #1e2d52', borderRadius: '12px', padding: '16px' }}>
          <h3>Signal Timeline</h3>
          <p>Synthetic observation stream active.</p>
          <p>Future support:
            BLE, LoRa, Wi-Fi, ADS-B, directional mapping.
          </p>
        </div>
      </div>
    </div>
  );
}
