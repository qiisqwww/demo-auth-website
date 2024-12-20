// import React from 'react'

interface IErrorProps{
	error:string
}

export default function ErrorMessage({error}:IErrorProps) {
	return (
		<div>
			<h2 style={{color: "rgba(255,80,80,1)", fontSize: 12, marginTop: 0}}>{error}</h2>
		</div>
	)
}
