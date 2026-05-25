# React Patterns Reference
# Deeper component patterns for when the SKILL.md basics aren't enough.
## Controlled Form
```tsx
function ContactForm() {
  const [form, setForm] = useState({ name: '', email: '' });
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm(prev => ({ ...prev, [e.target.name]: e.target.value }));
  };
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log(form);
  };
  return (
    <form onSubmit={handleSubmit}>
      <input name="name" value={form.name} onChange={handleChange} />
      <input name="email" value={form.email} onChange={handleChange} />
      <button type="submit">Send</button>
    </form>
  );
}
```
## Modal Pattern
```tsx
function Modal({ isOpen, onClose, children }: {
  isOpen: boolean;
  onClose: () => void;
  children: React.ReactNode;
}) {
  if (!isOpen) return null;
  return (
    <div className="overlay" onClick={onClose}>
      <div className="modal" onClick={e => e.stopPropagation()}>
        {children}
        <button onClick={onClose}>Close</button>
      </div>
    </div>
  );
}
// Usage
const [isOpen, setIsOpen] = useState(false);
<Modal isOpen={isOpen} onClose={() => setIsOpen(false)}>
  <p>Modal content here</p>
</Modal>
```
## Context API (global state — e.g. theme, user)
```tsx
// 1. Create context
const ThemeContext = createContext<'light' | 'dark'>('light');
// 2. Wrap your app
<ThemeContext.Provider value="dark">
  <App />
</ThemeContext.Provider>
// 3. Use anywhere inside
const theme = useContext(ThemeContext);
```
## Custom Hooks
```tsx
// useLocalStorage — persists state to browser storage
function useLocalStorage<T>(key: string, initial: T) {
  const [value, setValue] = useState<T>(() => {
    const stored = localStorage.getItem(key);
    return stored ? JSON.parse(stored) : initial;
  });
  const set = (newValue: T) => {
    setValue(newValue);
    localStorage.setItem(key, JSON.stringify(newValue));
  };
  return [value, set] as const;
}
// useDebounce — delay a value update (useful for search inputs)
function useDebounce<T>(value: T, delay: number): T {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const timer = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(timer);
  }, [value, delay]);
  return debounced;
}
```
