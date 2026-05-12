import { useMemo } from 'react'

const cards = [
  'Trending AI tools today',
  'Viral post variants',
  'Best-performing hooks',
  'Search trend snapshots'
]

export function App() {
  const timestamp = useMemo(() => new Date().toLocaleString('en-US'), [])

  return (
    <main className="app">
      <header>
        <h1>AI Trend Radar</h1>
        <p>Discover trending AI tools and generate viral X content in one click.</p>
        <small>Updated: {timestamp}</small>
      </header>

      <section className="grid">
        {cards.map((label) => (
          <article key={label} className="card">
            <h3>{label}</h3>
            <p>Creator-focused insights with engagement and virality scoring.</p>
          </article>
        ))}
      </section>
    </main>
  )
}
