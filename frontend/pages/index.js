import Head from "next/head";
import TeacherState from "../components/TeacherStats";
import Header from "../components/Header";

export async function getStaticProps() {
  const res = await fetch("http://localhost:8000/api/teachers/info");
  const data = await res.json();
  return {
    props: { data },
  };
}

export default function Home({ data }) {
  return (
    <div>
      <Head>
        <title>Ompractice</title>
        <link rel="icon" href="/favicon.ico" />
        <link
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
          rel="stylesheet"
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
          crossOrigin="anonymous"
        />
        <script
          src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js"
          integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW"
          crossOrigin="anonymous"
        ></script>
      </Head>
      <Header />
      <main className="container mt-5">
        <TeacherState info={data} />
      </main>
      <footer></footer>
    </div>
  );
}
