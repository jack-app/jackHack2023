import Head from "next/head";

export default function Home() {
  return (
    <>
      <div>
        <Head>
          <title>Next.js with TypeScript</title>
          <link rel="icon" href="/favicon.ico" />
        </Head>

        <h1 className="title">Homeです。</h1>
      </div>
      <style jsx>{`
        .title {
          font-size: 50px;
        }
      `}</style>
    </>
  );
}
