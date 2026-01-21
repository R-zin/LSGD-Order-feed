import LiquidEther from "../components/LiquidEther";
import SplitText from "../components/SplitText";
function Hero() {
    return(
        <div className="bg-black h-screen w-screen relative overflow-hidden">
  <div className="absolute inset-0 z-0">
    <LiquidEther
      colors={[ '#5227FF', '#FF9FFC', '#B19EEF' ]}
      mouseForce={20}
      cursorSize={100}
      isViscous={false}
      viscous={30}
      iterationsViscous={32}
      iterationsPoisson={32}
      resolution={0.5}
      isBounce={false}
      autoDemo={true}
      autoSpeed={0.5}
      autoIntensity={2.2}
      takeoverDuration={0.25}
      autoResumeDelay={3000}
      autoRampDuration={0.6}
    />
  </div>
  <div className="absolute inset-0 z-10 flex items-center justify-center m-auto">
  <SplitText
    className="text-9xl font-semibold text-center text-white"
    text="Tired of Waiting for Govt Orders?"
    delay={100}
    duration={0.6}
    ease="power3.out"
    splitType="chars"
    from={{ opacity: 0, y: 40 }}
    to={{ opacity: 1, y: 0 }}
    threshold={0.1}
    rootMargin="-100px"
    textAlign="center"
    >

    </SplitText>
    </div>
</div>
    )
}
export default Hero;