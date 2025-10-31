export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <head>
        <style>
          {`
            body {
              background-color: white;
              color: black;
              font-family: sans-serif;
            }
            main {
              max-width: 800px;
              margin: 0 auto;
            }
            table {
              width: 100%;
            }
            a {
              color: blue;
            }
          `}
        </style>
      </head>
      <body>{children}</body>
    </html>
  );
}
