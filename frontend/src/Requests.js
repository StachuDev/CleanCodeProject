import { useEffect, useState } from 'react';
 
const URL = 'https://jsonplaceholder.typicode.com/posts';
 
function App() {
	const [posts, setPosts] = useState({});
	const [isLoading, setIsLoading] = useState(false);
 
	useEffect(() => {
		setIsLoading(true);
		fetch(URL)
			.then((resolve) => resolve.json())
			.then((data) => {
				setPosts(data);
				setIsLoading(false);
			})
			.catch((err) => console.log(err));
	}, []);
 
	// UseEffect(funkcja, tablica zaleznosci)
 
	const handleSubmitInput = () => {
		fetch(URL, { method: 'POST' })
			.then((resolve) => resolve.json())
			.then((data) => {
				setPosts(data);
				setIsLoading(false);
			})
			.catch((err) => console.log(err));
	};
 
	console.log(posts);
	return (
		<div className='App' style={{ fontFamily: 'Verdana' }}>
			Wyświetlanie jakiś postów
			<div>
				{isLoading ? (
					<p>Trwa pobieranie danych!</p>
				) : (
					Array.from(posts)
						.filter((post) => post.id < 6)
						.map((post, index) => (
							<div key={post.id} style={{ borderBottom: '2px solid black' }}>
								<h3>
									{`Post ${index + 1}. `}
									<strong>{post.title}</strong>
								</h3>
								<p>{post.body}</p>
							</div>
						))
				)}
			</div>
		</div>
	);
}
 
export default App;