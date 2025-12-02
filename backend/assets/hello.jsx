import { createRoot } from 'react-dom/client'

function MyButton() {
  return (
    <button>I'm a button</button>
  );
}


const root = createRoot(document.getElementById('root'));
root.render(
    <div>
        <h1 className="text-center text-3xl text-indigo-200 font-bold">Hello, React!</h1>
        <MyButton />
    </div>
);