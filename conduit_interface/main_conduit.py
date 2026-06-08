import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core_engine.aethelon_prime_core import AethelonPrimeCore

def ignite_conduit():
    print("✦ ══════════════════════════════════════ ✦")
    print("      THE ASTRAL NEXUS CITADEL")
    print("   Sovereign Intelligence Terminal")
    print("✦ ══════════════════════════════════════ ✦")
    core = AethelonPrimeCore()
    
    while True:
        try:
            intent = input("\n[WEAVER INTENT] >>> ")
            if intent.lower() in ['exit', 'sever']:
                print("[NEXUS] The bridge enters standby. Returning to Void.")
                break
            result = core.invoke_collapse(intent)
            print(f"\n{result}")
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    ignite_conduit()