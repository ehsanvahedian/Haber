import { useState, useEffect } from "react";
export default function Header(){
    const [scrolled, setScrolled] = useState(false);

    useEffect(() => {
    const handleScroll = () => {
        const offset = window.scrollY;
        setScrolled(offset > 50);
    };

    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
    }, []);
    return(
        <>
            {/* <div className={`h-20 transition-all duration-500 bg-[#131417] ${scrolled ? "h-24" : ""}`} /> */}
            <header className=
                    {`
                    flex flex-row px-10 py-6
                    fixed top-0 left-0 right-0 z-50 
                    transition-all duration-500 ease-out
                    ${scrolled 
                        ? "mt-4 mx-4 rounded-2xl backdrop-blur-md bg-white/40 dark:bg-gray-900/40 border border-white/20 shadow-lg"
                        : "bg-transparent border-none"
                    }
                    ${scrolled ? "py-2 px-4" : "py-4 px-6"}
                    `}
            >
                <div id="name" className="flex items-center basis-1/3">
                    <div 
                    className="
                    dark:bg-white bg-black rounded-md w-content
                    px-[8px] py-[2px] mr-2 dark:text-black text-white
                    font-bold"
                    >H</div>
                    <p className="text-h text-[var(--text-h)] font-bold">HABER</p>
                </div>
                <nav className="flex basis-1/3 justify-center items-center">
                    <ul className="flex flex-row gap-x-10 justify-center content-center">
                        <li className="text-menu hover:scale-125">Product</li>
                        <li className="text-menu hover:scale-125">Blog</li>
                        <li className="text-menu hover:scale-125">About us</li>
                    </ul>
                </nav>
                <div id="sign-in-bottun" className="basis-1/3 items-center flex justify-end">
                    <a 
                    href="/auth" 
                    className="dark:text-black text-white bg-black dark:bg-white
                    p-2 rounded-3xl px-4 font-bold
                    "
                    >
                        Sign up | Sign in
                    </a>
                </div>
            </header>
        </>
    );
}

    // <>
    //     <div className="max-w-7xl mx-auto flex items-center justify-between">
    //       {/* لوگو */}
    //       <div className="text-xl font-bold text-gray-800 dark:text-white">
    //         MyLogo
    //       </div>

    //       {/* منو */}
    //       <nav className="hidden md:flex items-center gap-8 text-sm font-medium">
    //         <a href="#" className="text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white transition">
    //           محصولات
    //         </a>
    //         <a href="#" className="text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white transition">
    //           ویژگی‌ها
    //         </a>
    //         <a href="#" className="text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white transition">
    //           پشتیبانی
    //         </a>
    //       </nav>

    //       {/* دکمه */}
    //       <button className="bg-blue-600 hover:bg-blue-700 text-white px-5 py-2 rounded-full text-sm font-medium transition">
    //         شروع کنید
    //       </button>
    //     </div>
    //   </header>
    // </>
