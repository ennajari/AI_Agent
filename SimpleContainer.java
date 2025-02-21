import jade.core.Profile;
import jade.core.ProfileImpl;
import jade.core.Runtime;
import jade.wrapper.AgentContainer;
import jade.util.leap.Properties;

public class SimpleContainer {
    public static void main(String[] args) {
        try {
        // Get the JADE runtime instance
        Runtime rt = Runtime.instance();

        // Create a profile for the container
        Profile profile = new ProfileImpl(false); // false means this is not the main container
        profile.setParameter(Profile.MAIN_HOST, "localhost"); // Set the main host to localhost

        AgentContainer agentContainer = rt.createAgentContainer(profile);
        agentContainer.start();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
