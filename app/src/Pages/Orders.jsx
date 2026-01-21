import DecryptedText from "../components/DecryptedText";
import StaggeredMenu from "../components/StaggeredMenu";
const menuItems = [
  { label: 'Home', ariaLabel: 'Go to home page', link: '/' },
  { label: 'About', ariaLabel: 'Learn about us', link: '/about' },
  { label: 'Contact', ariaLabel: 'Get in touch', link: '/contact' }
];
const socialItems = [
  { label: 'Twitter', link: 'https://twitter.com' },
  { label: 'GitHub', link: 'https://github.com' },
  { label: 'LinkedIn', link: 'https://linkedin.com' }
];
function Orders() {
    return(
        <>
        <div className="bg-gray-950 min-h-screen">
        <div className="min-h-screen min-w-screen" style={{ height: '100vh', background: '#1a1a1a' }}>
        <StaggeredMenu
        position="right"
        socialItems={{socialItems}}
        items={menuItems}></StaggeredMenu>
        </div>
        </div>
        </>
    );
}
export default Orders;