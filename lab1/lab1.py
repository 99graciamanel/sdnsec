from mininet.cli import CLI
from mininet.link import TCLink
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.topo import Topo

# sudo mn --custom lab1.py --topo lab1
class Lab1(Topo):
    def __init__(self):
        # Initialize topology
        Topo.__init__(self)
        # Add hosts
        h1 = self.addHost('h1', ip='10.0.0.1')
        h2 = self.addHost('h2', ip='10.0.0.2')
        h3 = self.addHost('h3', ip='10.0.0.3')
        h4 = self.addHost('h4', ip='10.0.0.4')

        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        # Add (bidirectional) links
        self.addLink(s1, s2, cls=TCLink, bw=20, max_queu_size=500)
        self.addLink(h1, s1, cls=TCLink, bw=10, max_queu_size=500)
        self.addLink(h2, s1, cls=TCLink, bw=10, max_queu_size=500)
        self.addLink(h3, s2, cls=TCLink, bw=10, max_queu_size=500)
        self.addLink(h4, s2, cls=TCLink, bw=10, max_queu_size=500)

# Adding the 'topos' dict with a key/value pair to
topos = {'lab1': (lambda: Lab1())}


