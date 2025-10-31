import Link from "next/link";

interface Dog {
  id: number;
  breed: string;
  image: string;
}

async function getDogs(offset: number, limit: number): Promise<Dog[]> {
  const res = await fetch(`http://server:8000/api/dogs?offset=${offset}&limit=${limit}`, { cache: 'no-store' });
  if (!res.ok) {
    throw new Error("Failed to fetch dogs");
  }
  return res.json();
}

async function getDogsCount(): Promise<number> {
  const res = await fetch(`http://server:8000/api/dogs/count`, { cache: 'no-store' });
  if (!res.ok) {
    throw new Error("Failed to fetch dogs count");
  }
  const data = await res.json();
  return data.total;
}

export default async function Home({
  searchParams,
}: {
  searchParams?: { [key: string]: string | string[] | undefined };
}) {
  const offset = searchParams?.offset ? parseInt(searchParams.offset as string, 10) : 0;
  const limit = 15;
  const [dogs, totalDogs] = await Promise.all([
    getDogs(offset, limit),
    getDogsCount(),
  ]);

  const totalPages = Math.ceil(totalDogs / limit);
  const currentPage = Math.floor(offset / limit) + 1;

  const pages = Array.from({ length: totalPages }, (_, i) => i + 1);

  return (
    <main>
      <h1>Dog Breeds</h1>
      <table>
        <thead>
          <tr>
            <th>Breed</th>
            <th>Image</th>
          </tr>
        </thead>
        <tbody>
          {dogs.map((dog) => (
            <tr key={dog.id}>
              <td>{dog.breed}</td>
              <td>
                {dog.image ? (
                  <img src={dog.image} alt={dog.breed} width={100} />
                ) : (
                  "no image"
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <div>
        {currentPage > 1 && (
          <Link href={`/?offset=${offset - limit}`}>
            Previous
          </Link>
        )}
        {pages.map((page) => (
          <Link
            key={page}
            href={`/?offset=${(page - 1) * limit}`}
            style={{
              margin: "0 5px",
              fontWeight: currentPage === page ? "bold" : "normal",
            }}
          >
            {page}
          </Link>
        ))}
        {currentPage < totalPages && (
          <Link href={`/?offset=${offset + limit}`}>
            Next
          </Link>
        )}
      </div>
    </main>
  );
}