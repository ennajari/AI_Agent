import jade.core.Profile;
import jade.core.ProfileImpl;
import jade.core.Runtime;
import jade.wrapper.AgentContainer;
import jade.util.leap.Properties;

public class MainContainer {
    public static void main(String[] args) {
        // Get the JADE runtime instance
        Runtime rt = Runtime.instance();

        // Create a properties object to configure the platform
        Properties p = new Properties();
        p.setProperty("gui", "true"); // Enable the JADE GUI

        // Create a profile
        Profile prof = new ProfileImpl(p);

        // Create the main container
        AgentContainer container = rt.createMainContainer(prof);

        System.out.println("JADE platform started successfully.");
    }
}