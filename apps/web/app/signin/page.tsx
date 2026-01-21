import Link from 'next/link'
import React from 'react'

export default function SignIn() {
  const backend = process.env.NEXT_PUBLIC_SERVER_API;
  return (
    <>
      <h1>SignIn</h1>
      <Link href={backend + "/auth/google"}>Sign In</Link>
    </>
  )
}
