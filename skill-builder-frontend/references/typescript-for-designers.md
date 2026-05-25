# TypeScript for Designers
# Only what you need for component work. Nothing more.
## Typing Props
```tsx
interface ButtonProps {
  label: string;                          // required string
  variant?: 'primary' | 'secondary';     // optional, specific values only
  isDisabled?: boolean;                  // optional boolean
  onClick?: () => void;                  // optional function, no return value
  children?: React.ReactNode;            // optional slot (any JSX)
}
```
## Typing useState
```tsx
const [name, setName] = useState<string>('');
const [count, setCount] = useState<number>(0);
const [isOpen, setIsOpen] = useState<boolean>(false);
const [selected, setSelected] = useState<string | null>(null);  // can be null
```
## Typing Event Handlers
```tsx
// Input change
onChange={(e: React.ChangeEvent<HTMLInputElement>) => setValue(e.target.value)}
// Button click
onClick={(e: React.MouseEvent<HTMLButtonElement>) => handleClick()}
// Form submit
onSubmit={(e: React.FormEvent<HTMLFormElement>) => { e.preventDefault(); }}
```
## Typing an API Response
```tsx
interface User {
  id: number;
  name: string;
  email: string;
}
const [user, setUser] = useState<User | null>(null);
fetch('/api/user')
  .then(res => res.json())
  .then((data: User) => setUser(data));
```
## type vs interface
```tsx
// interface — for component props and objects (preferred)
interface CardProps { title: string; }
// type — for unions, aliases, computed types
type Status = 'active' | 'inactive' | 'pending';
type ID = string | number;
```
## Reading TypeScript Errors
- `Type 'X' is not assignable to type 'Y'` → you're passing the wrong kind of value
- `Property 'X' does not exist on type 'Y'` → typo in prop name, or prop not defined in interface
- `Object is possibly 'null'` → add a null check: `if (value) { ... }`
- `Parameter 'X' implicitly has an 'any' type` → add a type annotation to the function parameter
